using UnityEngine;
using System.Collections;
using System.Collections.Generic;
 

public class create_spheres : MonoBehaviour {
    void Awake() {
        Debug.Log("Sphere Builder Initiated");

        //Looad Sphere Material
        List<Dictionary<string,object>> data = CSVReader.Read ("circle_data_live");
        Material newMat = Resources.Load("Sphere", typeof(Material)) as Material;

        for(var i=0; i < data.Count; i++) {
            //Load CSV sphere position and size data
            var id = data[i]["ID"];
            var r = data[i]["RADIUS"];
            var x = data[i]["X"];
            var y = data[i]["Y"];
            var z = data[i]["Z"];

            //Convert to Floats
            float x_f = (float) x;
            float y_f = (float) y;
            //float z_f = (float) z;
            float r_f = (float) r; 

            //Create sphere with CSV data
            GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            sphere.transform.position = new Vector3(x_f, (y_f*-1), (1)); //20 is arbitraty number to ajust scale of Z axis
            sphere.transform.localScale = new Vector3(r_f*4, r_f*4, r_f*4);
            sphere.GetComponent<Renderer>().material = newMat;

            //set GameObject (sphere) name to its corresponding ID
            sphere.name = id.ToString();
          
        }

        Debug.Log("Sphere Builder Completed");

        

        
        
 

        
    }
 
    // Use this for initialization
    void Start () {
    }
 
    // Update is called once per frame
    void Update () {

        
        List<Dictionary<string,object>> data = CSVReader.Read ("circle_data_live");
        Material newMat = Resources.Load("Sphere", typeof(Material)) as Material;
        var i = 0;
        while(i < data.Count){
            //Load CSV sphere position and size data
            var id = data[i]["ID"];
            var r = data[i]["RADIUS"];
            var x = data[i]["X"];
            var y = data[i]["Y"];
            var z = data[i]["Z"];

            //Convert to Floats
            float x_f = (float) x;
            float y_f = (float) y;
            //float z_f = (float) z;
            float r_f = (float) r;

            GameObject sphereUpdate = GameObject.Find(id.ToString());
            sphereUpdate.transform.position = new Vector3(x_f, (y_f*-1), (1)); //20 is arbitraty number to ajust scale of Z axis
            sphereUpdate.transform.localScale = new Vector3(r_f, r_f, r_f);
            i=i+1;

        }   
    }
}
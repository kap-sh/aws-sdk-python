"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseConnectionUrls``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AutonomousDatabaseConnectionUrls(TypedDict):
    apex_url: NotRequired["str"]
    """<p>The URL for accessing Oracle Application Express (APEX) for the Autonomous Database.</p>"""
    database_transforms_url: NotRequired["str"]
    """<p>The URL for accessing Oracle Database Transforms for the Autonomous Database.</p>"""
    graph_studio_url: NotRequired["str"]
    """<p>The URL for accessing Oracle Graph Studio for the Autonomous Database.</p>"""
    machine_learning_notebook_url: NotRequired["str"]
    """<p>The URL for accessing the Oracle Machine Learning notebook for the Autonomous Database.</p>"""
    machine_learning_user_management_url: NotRequired["str"]
    """<p>The URL for accessing Oracle Machine Learning user management for the Autonomous Database.</p>"""
    mongo_db_url: NotRequired["str"]
    """<p>The URL for accessing the MongoDB API for the Autonomous Database.</p>"""
    ords_url: NotRequired["str"]
    """<p>The URL for accessing Oracle REST Data Services (ORDS) for the Autonomous Database.</p>"""
    spatial_studio_url: NotRequired["str"]
    """<p>The URL for accessing Oracle Spatial Studio for the Autonomous Database.</p>"""
    sql_dev_web_url: NotRequired["str"]
    """<p>The URL for accessing Oracle SQL Developer Web for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseConnectionUrls) -> dict:
    out: dict = {}
    if "apex_url" in value:
        out["apexUrl"] = value["apex_url"]
    if "database_transforms_url" in value:
        out["databaseTransformsUrl"] = value["database_transforms_url"]
    if "graph_studio_url" in value:
        out["graphStudioUrl"] = value["graph_studio_url"]
    if "machine_learning_notebook_url" in value:
        out["machineLearningNotebookUrl"] = value["machine_learning_notebook_url"]
    if "machine_learning_user_management_url" in value:
        out["machineLearningUserManagementUrl"] = value[
            "machine_learning_user_management_url"
        ]
    if "mongo_db_url" in value:
        out["mongoDbUrl"] = value["mongo_db_url"]
    if "ords_url" in value:
        out["ordsUrl"] = value["ords_url"]
    if "spatial_studio_url" in value:
        out["spatialStudioUrl"] = value["spatial_studio_url"]
    if "sql_dev_web_url" in value:
        out["sqlDevWebUrl"] = value["sql_dev_web_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseConnectionUrls:
    out: AutonomousDatabaseConnectionUrls = {}  # type: ignore[typeddict-item]
    if "apexUrl" in data:
        out["apex_url"] = data["apexUrl"]
    if "databaseTransformsUrl" in data:
        out["database_transforms_url"] = data["databaseTransformsUrl"]
    if "graphStudioUrl" in data:
        out["graph_studio_url"] = data["graphStudioUrl"]
    if "machineLearningNotebookUrl" in data:
        out["machine_learning_notebook_url"] = data["machineLearningNotebookUrl"]
    if "machineLearningUserManagementUrl" in data:
        out["machine_learning_user_management_url"] = data[
            "machineLearningUserManagementUrl"
        ]
    if "mongoDbUrl" in data:
        out["mongo_db_url"] = data["mongoDbUrl"]
    if "ordsUrl" in data:
        out["ords_url"] = data["ordsUrl"]
    if "spatialStudioUrl" in data:
        out["spatial_studio_url"] = data["spatialStudioUrl"]
    if "sqlDevWebUrl" in data:
        out["sql_dev_web_url"] = data["sqlDevWebUrl"]
    return out

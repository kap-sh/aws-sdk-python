"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.count
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.role_arn
    import aws_sdk_lex_models_v2.types.test_set_modality
    import aws_sdk_lex_models_v2.types.test_set_status
    import aws_sdk_lex_models_v2.types.test_set_storage_location
    import aws_sdk_lex_models_v2.types.timestamp


class TestSetSummary(TypedDict):
    test_set_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set.</p>"""
    test_set_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the test set.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description of the test set.</p>"""
    modality: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_modality.TestSetModality"
    ]
    """<p>Specifies whether the test set contains written or spoken data.</p>"""
    status: NotRequired["aws_sdk_lex_models_v2.types.test_set_status.TestSetStatus"]
    """<p>The status of the test set.</p>"""
    role_arn: NotRequired["aws_sdk_lex_models_v2.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the test set.</p>"""
    num_turns: NotRequired["aws_sdk_lex_models_v2.types.count.Count"]
    """<p>The number of turns in the test set.</p>"""
    storage_location: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_storage_location.TestSetStorageLocation"
    ]
    """<p>Contains information about the location at which the test set is stored.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the test set was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time at which the test set was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetSummary) -> dict:
    out: dict = {}
    if "test_set_id" in value:
        out["testSetId"] = value["test_set_id"]
    if "test_set_name" in value:
        out["testSetName"] = value["test_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "modality" in value:
        import aws_sdk_lex_models_v2.types.test_set_modality

        out["modality"] = aws_sdk_lex_models_v2.types.test_set_modality.serialize_json(
            value["modality"]
        )
    if "status" in value:
        import aws_sdk_lex_models_v2.types.test_set_status

        out["status"] = aws_sdk_lex_models_v2.types.test_set_status.serialize_json(
            value["status"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "num_turns" in value:
        out["numTurns"] = value["num_turns"]
    if "storage_location" in value:
        import aws_sdk_lex_models_v2.types.test_set_storage_location

        out["storageLocation"] = (
            aws_sdk_lex_models_v2.types.test_set_storage_location.serialize_json(
                value["storage_location"]
            )
        )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestSetSummary:
    out: TestSetSummary = {}  # type: ignore[typeddict-item]
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
    if "testSetName" in data:
        out["test_set_name"] = data["testSetName"]
    if "description" in data:
        out["description"] = data["description"]
    if "modality" in data:
        import aws_sdk_lex_models_v2.types.test_set_modality

        out["modality"] = (
            aws_sdk_lex_models_v2.types.test_set_modality.deserialize_json(
                data["modality"]
            )
        )
    if "status" in data:
        import aws_sdk_lex_models_v2.types.test_set_status

        out["status"] = aws_sdk_lex_models_v2.types.test_set_status.deserialize_json(
            data["status"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "numTurns" in data:
        out["num_turns"] = data["numTurns"]
    if "storageLocation" in data:
        import aws_sdk_lex_models_v2.types.test_set_storage_location

        out["storage_location"] = (
            aws_sdk_lex_models_v2.types.test_set_storage_location.deserialize_json(
                data["storageLocation"]
            )
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out

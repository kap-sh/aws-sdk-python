"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartTestSetGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.role_arn
    import aws_sdk_lex_models_v2.types.tag_map
    import aws_sdk_lex_models_v2.types.test_set_generation_data_source
    import aws_sdk_lex_models_v2.types.test_set_generation_status
    import aws_sdk_lex_models_v2.types.test_set_storage_location
    import aws_sdk_lex_models_v2.types.timestamp


class StartTestSetGenerationResponse(TypedDict, closed=True):
    test_set_generation_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set generation to describe.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p> The creation date and time for the test set generation.</p>"""
    test_set_generation_status: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_generation_status.TestSetGenerationStatus"
    ]
    """<p> The status for the test set generation.</p>"""
    test_set_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The test set name used for the test set generation.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description used for the test set generation.</p>"""
    storage_location: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_storage_location.TestSetStorageLocation"
    ]
    """<p>The Amazon S3 storage location for the test set generation.</p>"""
    generation_data_source: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_generation_data_source.TestSetGenerationDataSource"
    ]
    """<p> The data source for the test set generation.</p>"""
    role_arn: NotRequired["aws_sdk_lex_models_v2.types.role_arn.RoleArn"]
    """<p>The roleARN used for any operation in the test set to access resources in the Amazon Web Services account.</p>"""
    test_set_tags: NotRequired["aws_sdk_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags that was used for the test set that is being generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestSetGenerationResponse) -> dict:
    out: dict = {}
    if "test_set_generation_id" in value:
        out["testSetGenerationId"] = value["test_set_generation_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "test_set_generation_status" in value:
        import aws_sdk_lex_models_v2.types.test_set_generation_status

        out["testSetGenerationStatus"] = (
            aws_sdk_lex_models_v2.types.test_set_generation_status.serialize_json(
                value["test_set_generation_status"]
            )
        )
    if "test_set_name" in value:
        out["testSetName"] = value["test_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "storage_location" in value:
        import aws_sdk_lex_models_v2.types.test_set_storage_location

        out["storageLocation"] = (
            aws_sdk_lex_models_v2.types.test_set_storage_location.serialize_json(
                value["storage_location"]
            )
        )
    if "generation_data_source" in value:
        import aws_sdk_lex_models_v2.types.test_set_generation_data_source

        out["generationDataSource"] = (
            aws_sdk_lex_models_v2.types.test_set_generation_data_source.serialize_json(
                value["generation_data_source"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "test_set_tags" in value:
        import aws_sdk_lex_models_v2.types.tag_map

        out["testSetTags"] = aws_sdk_lex_models_v2.types.tag_map.serialize_json(
            value["test_set_tags"]
        )
    return out


def deserialize_json(data: dict) -> StartTestSetGenerationResponse:
    out: StartTestSetGenerationResponse = {}  # type: ignore[typeddict-item]
    if "testSetGenerationId" in data:
        out["test_set_generation_id"] = data["testSetGenerationId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "testSetGenerationStatus" in data:
        import aws_sdk_lex_models_v2.types.test_set_generation_status

        out["test_set_generation_status"] = (
            aws_sdk_lex_models_v2.types.test_set_generation_status.deserialize_json(
                data["testSetGenerationStatus"]
            )
        )
    if "testSetName" in data:
        out["test_set_name"] = data["testSetName"]
    if "description" in data:
        out["description"] = data["description"]
    if "storageLocation" in data:
        import aws_sdk_lex_models_v2.types.test_set_storage_location

        out["storage_location"] = (
            aws_sdk_lex_models_v2.types.test_set_storage_location.deserialize_json(
                data["storageLocation"]
            )
        )
    if "generationDataSource" in data:
        import aws_sdk_lex_models_v2.types.test_set_generation_data_source

        out["generation_data_source"] = (
            aws_sdk_lex_models_v2.types.test_set_generation_data_source.deserialize_json(
                data["generationDataSource"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "testSetTags" in data:
        import aws_sdk_lex_models_v2.types.tag_map

        out["test_set_tags"] = aws_sdk_lex_models_v2.types.tag_map.deserialize_json(
            data["testSetTags"]
        )
    return out

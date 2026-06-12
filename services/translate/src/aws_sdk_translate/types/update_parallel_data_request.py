"""Generated from Smithy shape ``com.amazonaws.translate#UpdateParallelDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.client_token_string
    import aws_sdk_translate.types.description
    import aws_sdk_translate.types.parallel_data_config
    import aws_sdk_translate.types.resource_name


class UpdateParallelDataRequest(TypedDict):
    name: "aws_sdk_translate.types.resource_name.ResourceName"
    """<p>The name of the parallel data resource being updated.</p>"""
    description: NotRequired["aws_sdk_translate.types.description.Description"]
    """<p>A custom description for the parallel data resource in Amazon Translate.</p>"""
    parallel_data_config: (
        "aws_sdk_translate.types.parallel_data_config.ParallelDataConfig"
    )
    """<p>Specifies the format and S3 location of the parallel data input file.</p>"""
    client_token: "aws_sdk_translate.types.client_token_string.ClientTokenString"
    """<p>A unique identifier for the request. This token is automatically generated when you use Amazon Translate through an AWS SDK.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParallelDataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_translate.types.parallel_data_config

    out["ParallelDataConfig"] = (
        aws_sdk_translate.types.parallel_data_config.serialize_aws_json_1_1(
            value["parallel_data_config"]
        )
    )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParallelDataRequest:
    out: UpdateParallelDataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateParallelDataRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ParallelDataConfig" in data:
        import aws_sdk_translate.types.parallel_data_config

        out["parallel_data_config"] = (
            aws_sdk_translate.types.parallel_data_config.deserialize_aws_json_1_1(
                data["ParallelDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateParallelDataRequest.parallel_data_config required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("UpdateParallelDataRequest.client_token required")
    return out

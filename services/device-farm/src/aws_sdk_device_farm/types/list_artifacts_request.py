"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListArtifactsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.artifact_category
    import aws_sdk_device_farm.types.pagination_token


class ListArtifactsRequest(TypedDict):
    arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The run, job, suite, or test ARN.</p>"""
    type: "aws_sdk_device_farm.types.artifact_category.ArtifactCategory"
    """<p>The artifacts' type.</p> <p>Allowed values include:</p> <ul> <li> <p>FILE</p> </li> <li> <p>LOG</p> </li> <li> <p>SCREENSHOT</p> </li> </ul>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArtifactsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_device_farm.types.artifact_category

    out["type"] = aws_sdk_device_farm.types.artifact_category.serialize_aws_json_1_1(
        value["type"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArtifactsRequest:
    out: ListArtifactsRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListArtifactsRequest.arn required")
    if "type" in data:
        import aws_sdk_device_farm.types.artifact_category

        out["type"] = (
            aws_sdk_device_farm.types.artifact_category.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ListArtifactsRequest.type required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

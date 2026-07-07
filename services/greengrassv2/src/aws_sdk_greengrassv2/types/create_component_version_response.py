"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CreateComponentVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.cloud_component_status
    import aws_sdk_greengrassv2.types.component_name_string
    import aws_sdk_greengrassv2.types.component_version_arn
    import aws_sdk_greengrassv2.types.component_version_string
    import aws_sdk_greengrassv2.types.timestamp


class CreateComponentVersionResponse(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_arn.ComponentVersionARN"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.</p>"""
    component_name: (
        "aws_sdk_greengrassv2.types.component_name_string.ComponentNameString"
    )
    """<p>The name of the component.</p>"""
    component_version: (
        "aws_sdk_greengrassv2.types.component_version_string.ComponentVersionString"
    )
    """<p>The version of the component.</p>"""
    creation_timestamp: "aws_sdk_greengrassv2.types.timestamp.Timestamp"
    """<p>The time at which the component was created, expressed in ISO 8601 format.</p>"""
    status: "aws_sdk_greengrassv2.types.cloud_component_status.CloudComponentStatus"
    """<p>The status of the component version in IoT Greengrass V2. This status is different from the status of the component on a core device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentVersionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    out["componentName"] = value["component_name"]
    out["componentVersion"] = value["component_version"]
    import aws_sdk_greengrassv2.types.timestamp

    out["creationTimestamp"] = aws_sdk_greengrassv2.types.timestamp.serialize_json(
        value["creation_timestamp"]
    )
    import aws_sdk_greengrassv2.types.cloud_component_status

    out["status"] = aws_sdk_greengrassv2.types.cloud_component_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateComponentVersionResponse:
    out: CreateComponentVersionResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    else:
        raise DeserializationError(
            "CreateComponentVersionResponse.component_name required"
        )
    if "componentVersion" in data:
        out["component_version"] = data["componentVersion"]
    else:
        raise DeserializationError(
            "CreateComponentVersionResponse.component_version required"
        )
    if "creationTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["creation_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["creationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "CreateComponentVersionResponse.creation_timestamp required"
        )
    if "status" in data:
        import aws_sdk_greengrassv2.types.cloud_component_status

        out["status"] = (
            aws_sdk_greengrassv2.types.cloud_component_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateComponentVersionResponse.status required")
    return out

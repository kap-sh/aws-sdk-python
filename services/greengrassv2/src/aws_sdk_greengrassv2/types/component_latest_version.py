"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentLatestVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_platform_list
    import aws_sdk_greengrassv2.types.component_version_arn
    import aws_sdk_greengrassv2.types.component_version_string
    import aws_sdk_greengrassv2.types.non_empty_string
    import aws_sdk_greengrassv2.types.timestamp


class ComponentLatestVersion(TypedDict):
    arn: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_arn.ComponentVersionARN"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.</p>"""
    component_version: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    creation_timestamp: NotRequired["aws_sdk_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time at which the component was created, expressed in ISO 8601 format.</p>"""
    description: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the component version.</p>"""
    publisher: NotRequired["aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The publisher of the component version.</p>"""
    platforms: NotRequired[
        "aws_sdk_greengrassv2.types.component_platform_list.ComponentPlatformList"
    ]
    """<p>The platforms that the component version supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentLatestVersion) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "creation_timestamp" in value:
        import aws_sdk_greengrassv2.types.timestamp

        out["creationTimestamp"] = aws_sdk_greengrassv2.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "publisher" in value:
        out["publisher"] = value["publisher"]
    if "platforms" in value:
        import aws_sdk_greengrassv2.types.component_platform_list

        out["platforms"] = (
            aws_sdk_greengrassv2.types.component_platform_list.serialize_json(
                value["platforms"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentLatestVersion:
    out: ComponentLatestVersion = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "componentVersion" in data:
        out["component_version"] = data["componentVersion"]
    if "creationTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["creation_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["creationTimestamp"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "publisher" in data:
        out["publisher"] = data["publisher"]
    if "platforms" in data:
        import aws_sdk_greengrassv2.types.component_platform_list

        out["platforms"] = (
            aws_sdk_greengrassv2.types.component_platform_list.deserialize_json(
                data["platforms"]
            )
        )
    return out

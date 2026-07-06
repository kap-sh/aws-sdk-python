"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.scan_name_arn
    import aws_sdk_codeguru_security.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_codeguru_security.types.scan_name_arn.ScanNameArn"
    """<p>The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>CreateScan</code>, <code>ListScans</code>, or <code>GetScan</code>.</p>"""
    tags: "aws_sdk_codeguru_security.types.tag_map.TagMap"
    """<p>An array of key-value pairs used to tag an existing scan. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A tag key. For example, <code>CostCenter</code>, <code>Environment</code>, or <code>Secret</code>. Tag keys are case sensitive.</p> </li> <li> <p>An optional tag value field. For example, <code>111122223333</code>, <code>Production</code>, or a team name. Omitting the tag value is the same as using an empty string. Tag values are case sensitive.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_codeguru_security.types.tag_map

    out["tags"] = aws_sdk_codeguru_security.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codeguru_security.types.tag_map

        out["tags"] = aws_sdk_codeguru_security.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

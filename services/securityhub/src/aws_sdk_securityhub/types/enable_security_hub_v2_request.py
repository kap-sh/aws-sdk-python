"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableSecurityHubV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.tag_map


class EnableSecurityHubV2Request(TypedDict):
    tags: NotRequired["aws_sdk_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the hub V2 resource when you enable Security Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableSecurityHubV2Request) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_securityhub.types.tag_map

        out["Tags"] = aws_sdk_securityhub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EnableSecurityHubV2Request:
    out: EnableSecurityHubV2Request = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_securityhub.types.tag_map

        out["tags"] = aws_sdk_securityhub.types.tag_map.deserialize_json(data["Tags"])
    return out

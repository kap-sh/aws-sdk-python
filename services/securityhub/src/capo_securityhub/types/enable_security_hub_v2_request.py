"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableSecurityHubV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.tag_map


class EnableSecurityHubV2Request(TypedDict, closed=True):
    tags: NotRequired["capo_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the hub V2 resource when you enable Security Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableSecurityHubV2Request) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_securityhub.types.tag_map

        out["Tags"] = capo_securityhub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EnableSecurityHubV2Request:
    out: EnableSecurityHubV2Request = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_securityhub.types.tag_map

        out["tags"] = capo_securityhub.types.tag_map.deserialize_json(data["Tags"])
    return out

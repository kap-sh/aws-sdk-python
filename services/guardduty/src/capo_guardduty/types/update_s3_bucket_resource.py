"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateS3BucketResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.malware_protection_plan_object_prefixes_list


class UpdateS3BucketResource(TypedDict, closed=True):
    object_prefixes: NotRequired[
        "capo_guardduty.types.malware_protection_plan_object_prefixes_list.MalwareProtectionPlanObjectPrefixesList"
    ]
    """<p>Information about the specified object prefixes. The S3 object will be scanned only if it belongs to any of the specified object prefixes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateS3BucketResource) -> dict:
    out: dict = {}
    if "object_prefixes" in value:
        import capo_guardduty.types.malware_protection_plan_object_prefixes_list

        out["objectPrefixes"] = (
            capo_guardduty.types.malware_protection_plan_object_prefixes_list.serialize_json(
                value["object_prefixes"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateS3BucketResource:
    out: UpdateS3BucketResource = {}  # type: ignore[typeddict-item]
    if "objectPrefixes" in data:
        import capo_guardduty.types.malware_protection_plan_object_prefixes_list

        out["object_prefixes"] = (
            capo_guardduty.types.malware_protection_plan_object_prefixes_list.deserialize_json(
                data["objectPrefixes"]
            )
        )
    return out

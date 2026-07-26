"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessKeyLastUsed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.string


class AccessKeyLastUsed(TypedDict, closed=True):
    last_used_date: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The date and time when the access key was most recently used.</p> <p>This value is null if the access key has not been used.</p>"""
    region: NotRequired["capo_lightsail.types.string.string"]
    """<p>The Amazon Web Services Region where this access key was most recently used.</p> <p>This value is <code>N/A</code> if the access key has not been used.</p>"""
    service_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the Amazon Web Services service with which this access key was most recently used.</p> <p>This value is <code>N/A</code> if the access key has not been used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessKeyLastUsed) -> dict:
    out: dict = {}
    if "last_used_date" in value:
        import capo_lightsail.types.iso_date

        out["lastUsedDate"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["last_used_date"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessKeyLastUsed:
    out: AccessKeyLastUsed = {}  # type: ignore[typeddict-item]
    if "lastUsedDate" in data:
        import capo_lightsail.types.iso_date

        out["last_used_date"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["lastUsedDate"]
        )
    if "region" in data:
        out["region"] = data["region"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    return out

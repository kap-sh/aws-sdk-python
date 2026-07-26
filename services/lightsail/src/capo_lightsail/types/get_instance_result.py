"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance


class GetInstanceResult(TypedDict, closed=True):
    instance: NotRequired["capo_lightsail.types.instance.Instance"]
    """<p>An array of key-value pairs containing information about the specified instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceResult) -> dict:
    out: dict = {}
    if "instance" in value:
        import capo_lightsail.types.instance

        out["instance"] = capo_lightsail.types.instance.serialize_aws_json_1_1(
            value["instance"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceResult:
    out: GetInstanceResult = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import capo_lightsail.types.instance

        out["instance"] = capo_lightsail.types.instance.deserialize_aws_json_1_1(
            data["instance"]
        )
    return out

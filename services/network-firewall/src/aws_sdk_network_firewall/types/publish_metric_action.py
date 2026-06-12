"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PublishMetricAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.dimensions


class PublishMetricAction(TypedDict):
    dimensions: "aws_sdk_network_firewall.types.dimensions.Dimensions"
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishMetricAction) -> dict:
    out: dict = {}
    import aws_sdk_network_firewall.types.dimensions

    out["Dimensions"] = (
        aws_sdk_network_firewall.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PublishMetricAction:
    out: PublishMetricAction = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_network_firewall.types.dimensions

        out["dimensions"] = (
            aws_sdk_network_firewall.types.dimensions.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    else:
        raise DeserializationError("PublishMetricAction.dimensions required")
    return out

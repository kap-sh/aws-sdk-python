"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetResource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.aws_region
    import aws_sdk_networkflowmonitor.types.target_identifier


class TargetResource(TypedDict):
    target_identifier: (
        "aws_sdk_networkflowmonitor.types.target_identifier.TargetIdentifier"
    )
    """<p>A target identifier is a pair of identifying information for a scope. A target identifier is made up of a targetID (currently always an account ID) and a targetType (currently always an account).</p>"""
    region: "aws_sdk_networkflowmonitor.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region for the scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResource) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.target_identifier

    out["targetIdentifier"] = (
        aws_sdk_networkflowmonitor.types.target_identifier.serialize_json(
            value["target_identifier"]
        )
    )
    out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> TargetResource:
    out: TargetResource = {}  # type: ignore[typeddict-item]
    if "targetIdentifier" in data:
        import aws_sdk_networkflowmonitor.types.target_identifier

        out["target_identifier"] = (
            aws_sdk_networkflowmonitor.types.target_identifier.deserialize_json(
                data["targetIdentifier"]
            )
        )
    else:
        raise DeserializationError("TargetResource.target_identifier required")
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("TargetResource.region required")
    return out

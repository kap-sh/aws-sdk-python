"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlDriftTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_control_inheritance_drift
    import aws_sdk_controltower.types.enabled_control_resource_drift


class EnabledControlDriftTypes(TypedDict, closed=True):
    inheritance: NotRequired[
        "aws_sdk_controltower.types.enabled_control_inheritance_drift.EnabledControlInheritanceDrift"
    ]
    """<p>Indicates drift related to inheritance configuration between parent and child controls.</p>"""
    resource: NotRequired[
        "aws_sdk_controltower.types.enabled_control_resource_drift.EnabledControlResourceDrift"
    ]
    """<p>Indicates drift related to the underlying Amazon Web Services resources managed by the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlDriftTypes) -> dict:
    out: dict = {}
    if "inheritance" in value:
        import aws_sdk_controltower.types.enabled_control_inheritance_drift

        out["inheritance"] = (
            aws_sdk_controltower.types.enabled_control_inheritance_drift.serialize_json(
                value["inheritance"]
            )
        )
    if "resource" in value:
        import aws_sdk_controltower.types.enabled_control_resource_drift

        out["resource"] = (
            aws_sdk_controltower.types.enabled_control_resource_drift.serialize_json(
                value["resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledControlDriftTypes:
    out: EnabledControlDriftTypes = {}  # type: ignore[typeddict-item]
    if "inheritance" in data:
        import aws_sdk_controltower.types.enabled_control_inheritance_drift

        out["inheritance"] = (
            aws_sdk_controltower.types.enabled_control_inheritance_drift.deserialize_json(
                data["inheritance"]
            )
        )
    if "resource" in data:
        import aws_sdk_controltower.types.enabled_control_resource_drift

        out["resource"] = (
            aws_sdk_controltower.types.enabled_control_resource_drift.deserialize_json(
                data["resource"]
            )
        )
    return out

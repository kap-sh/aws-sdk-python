"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_inheritance_drift


class EnabledBaselineDriftTypes(TypedDict, closed=True):
    inheritance: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_inheritance_drift.EnabledBaselineInheritanceDrift"
    ]
    """<p>At least one account within the target OU does not match the baseline configuration defined on that OU. An account is in inheritance drift when it does not match the configuration of a parent OU, possibly a new parent OU, if the account is moved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDriftTypes) -> dict:
    out: dict = {}
    if "inheritance" in value:
        import aws_sdk_controltower.types.enabled_baseline_inheritance_drift

        out["inheritance"] = (
            aws_sdk_controltower.types.enabled_baseline_inheritance_drift.serialize_json(
                value["inheritance"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineDriftTypes:
    out: EnabledBaselineDriftTypes = {}  # type: ignore[typeddict-item]
    if "inheritance" in data:
        import aws_sdk_controltower.types.enabled_baseline_inheritance_drift

        out["inheritance"] = (
            aws_sdk_controltower.types.enabled_baseline_inheritance_drift.deserialize_json(
                data["inheritance"]
            )
        )
    return out

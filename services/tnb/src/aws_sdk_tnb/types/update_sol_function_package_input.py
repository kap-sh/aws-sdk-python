"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolFunctionPackageInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.operational_state
    import aws_sdk_tnb.types.vnf_pkg_id


class UpdateSolFunctionPackageInput(TypedDict):
    vnf_pkg_id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""
    operational_state: "aws_sdk_tnb.types.operational_state.OperationalState"
    """<p>Operational state of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolFunctionPackageInput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.operational_state

    out["operationalState"] = aws_sdk_tnb.types.operational_state.serialize_json(
        value["operational_state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSolFunctionPackageInput:
    out: UpdateSolFunctionPackageInput = {}  # type: ignore[typeddict-item]
    if "operationalState" in data:
        import aws_sdk_tnb.types.operational_state

        out["operational_state"] = aws_sdk_tnb.types.operational_state.deserialize_json(
            data["operationalState"]
        )
    else:
        raise DeserializationError(
            "UpdateSolFunctionPackageInput.operational_state required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.nsd_operational_state


class UpdateSolNetworkPackageInput(TypedDict, closed=True):
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    nsd_operational_state: "aws_sdk_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Operational state of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkPackageInput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.nsd_operational_state

    out["nsdOperationalState"] = aws_sdk_tnb.types.nsd_operational_state.serialize_json(
        value["nsd_operational_state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkPackageInput:
    out: UpdateSolNetworkPackageInput = {}  # type: ignore[typeddict-item]
    if "nsdOperationalState" in data:
        import aws_sdk_tnb.types.nsd_operational_state

        out["nsd_operational_state"] = (
            aws_sdk_tnb.types.nsd_operational_state.deserialize_json(
                data["nsdOperationalState"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSolNetworkPackageInput.nsd_operational_state required"
        )
    return out

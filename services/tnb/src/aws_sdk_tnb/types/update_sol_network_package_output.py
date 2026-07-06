"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkPackageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_operational_state


class UpdateSolNetworkPackageOutput(TypedDict, closed=True):
    nsd_operational_state: "aws_sdk_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Operational state of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkPackageOutput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.nsd_operational_state

    out["nsdOperationalState"] = aws_sdk_tnb.types.nsd_operational_state.serialize_json(
        value["nsd_operational_state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkPackageOutput:
    out: UpdateSolNetworkPackageOutput = {}  # type: ignore[typeddict-item]
    if "nsdOperationalState" in data:
        import aws_sdk_tnb.types.nsd_operational_state

        out["nsd_operational_state"] = (
            aws_sdk_tnb.types.nsd_operational_state.deserialize_json(
                data["nsdOperationalState"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSolNetworkPackageOutput.nsd_operational_state required"
        )
    return out

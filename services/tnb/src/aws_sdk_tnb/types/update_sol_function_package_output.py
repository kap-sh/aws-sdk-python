"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolFunctionPackageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.operational_state


class UpdateSolFunctionPackageOutput(TypedDict):
    operational_state: "aws_sdk_tnb.types.operational_state.OperationalState"
    """<p>Operational state of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolFunctionPackageOutput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.operational_state

    out["operationalState"] = aws_sdk_tnb.types.operational_state.serialize_json(
        value["operational_state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSolFunctionPackageOutput:
    out: UpdateSolFunctionPackageOutput = {}  # type: ignore[typeddict-item]
    if "operationalState" in data:
        import aws_sdk_tnb.types.operational_state

        out["operational_state"] = aws_sdk_tnb.types.operational_state.deserialize_json(
            data["operationalState"]
        )
    else:
        raise DeserializationError(
            "UpdateSolFunctionPackageOutput.operational_state required"
        )
    return out

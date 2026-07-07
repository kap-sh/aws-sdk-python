"""Generated from Smithy shape ``com.amazonaws.iotwireless#SemtechGnssDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.position_configuration_fec
    import aws_sdk_iot_wireless.types.position_configuration_status
    import aws_sdk_iot_wireless.types.position_solver_provider
    import aws_sdk_iot_wireless.types.position_solver_type


class SemtechGnssDetail(TypedDict, closed=True):
    provider: NotRequired[
        "aws_sdk_iot_wireless.types.position_solver_provider.PositionSolverProvider"
    ]
    """<p>The vendor of the solver object.</p>"""
    type: NotRequired[
        "aws_sdk_iot_wireless.types.position_solver_type.PositionSolverType"
    ]
    """<p>The type of positioning solver used.</p>"""
    status: NotRequired[
        "aws_sdk_iot_wireless.types.position_configuration_status.PositionConfigurationStatus"
    ]
    """<p>The status indicating whether the solver is enabled.</p>"""
    fec: NotRequired[
        "aws_sdk_iot_wireless.types.position_configuration_fec.PositionConfigurationFec"
    ]
    """<p>Whether forward error correction is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemtechGnssDetail) -> dict:
    out: dict = {}
    if "provider" in value:
        import aws_sdk_iot_wireless.types.position_solver_provider

        out["Provider"] = (
            aws_sdk_iot_wireless.types.position_solver_provider.serialize_json(
                value["provider"]
            )
        )
    if "type" in value:
        import aws_sdk_iot_wireless.types.position_solver_type

        out["Type"] = aws_sdk_iot_wireless.types.position_solver_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_iot_wireless.types.position_configuration_status

        out["Status"] = (
            aws_sdk_iot_wireless.types.position_configuration_status.serialize_json(
                value["status"]
            )
        )
    if "fec" in value:
        import aws_sdk_iot_wireless.types.position_configuration_fec

        out["Fec"] = (
            aws_sdk_iot_wireless.types.position_configuration_fec.serialize_json(
                value["fec"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemtechGnssDetail:
    out: SemtechGnssDetail = {}  # type: ignore[typeddict-item]
    if "Provider" in data:
        import aws_sdk_iot_wireless.types.position_solver_provider

        out["provider"] = (
            aws_sdk_iot_wireless.types.position_solver_provider.deserialize_json(
                data["Provider"]
            )
        )
    if "Type" in data:
        import aws_sdk_iot_wireless.types.position_solver_type

        out["type"] = aws_sdk_iot_wireless.types.position_solver_type.deserialize_json(
            data["Type"]
        )
    if "Status" in data:
        import aws_sdk_iot_wireless.types.position_configuration_status

        out["status"] = (
            aws_sdk_iot_wireless.types.position_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    if "Fec" in data:
        import aws_sdk_iot_wireless.types.position_configuration_fec

        out["fec"] = (
            aws_sdk_iot_wireless.types.position_configuration_fec.deserialize_json(
                data["Fec"]
            )
        )
    return out

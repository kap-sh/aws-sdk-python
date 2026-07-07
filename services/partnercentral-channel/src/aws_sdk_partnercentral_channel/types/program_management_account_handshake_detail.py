"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountHandshakeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program


class ProgramManagementAccountHandshakeDetail(TypedDict, closed=True):
    program: NotRequired["aws_sdk_partnercentral_channel.types.program.Program"]
    """<p>The program associated with the handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountHandshakeDetail) -> dict:
    out: dict = {}
    if "program" in value:
        import aws_sdk_partnercentral_channel.types.program

        out["program"] = (
            aws_sdk_partnercentral_channel.types.program.serialize_aws_json_1_0(
                value["program"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgramManagementAccountHandshakeDetail:
    out: ProgramManagementAccountHandshakeDetail = {}  # type: ignore[typeddict-item]
    if "program" in data:
        import aws_sdk_partnercentral_channel.types.program

        out["program"] = (
            aws_sdk_partnercentral_channel.types.program.deserialize_aws_json_1_0(
                data["program"]
            )
        )
    return out

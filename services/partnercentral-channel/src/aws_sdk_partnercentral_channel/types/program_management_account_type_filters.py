"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountTypeFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program_list


class ProgramManagementAccountTypeFilters(TypedDict):
    programs: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_list.ProgramList"
    ]
    """<p>Filter by program types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountTypeFilters) -> dict:
    out: dict = {}
    if "programs" in value:
        import aws_sdk_partnercentral_channel.types.program_list

        out["programs"] = (
            aws_sdk_partnercentral_channel.types.program_list.serialize_aws_json_1_0(
                value["programs"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgramManagementAccountTypeFilters:
    out: ProgramManagementAccountTypeFilters = {}  # type: ignore[typeddict-item]
    if "programs" in data:
        import aws_sdk_partnercentral_channel.types.program_list

        out["programs"] = (
            aws_sdk_partnercentral_channel.types.program_list.deserialize_aws_json_1_0(
                data["programs"]
            )
        )
    return out

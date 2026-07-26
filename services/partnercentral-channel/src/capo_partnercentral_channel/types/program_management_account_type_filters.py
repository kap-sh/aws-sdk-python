"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountTypeFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_list


class ProgramManagementAccountTypeFilters(TypedDict, closed=True):
    programs: NotRequired["capo_partnercentral_channel.types.program_list.ProgramList"]
    """<p>Filter by program types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountTypeFilters) -> dict:
    out: dict = {}
    if "programs" in value:
        import capo_partnercentral_channel.types.program_list

        out["programs"] = (
            capo_partnercentral_channel.types.program_list.serialize_aws_json_1_0(
                value["programs"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgramManagementAccountTypeFilters:
    out: ProgramManagementAccountTypeFilters = {}  # type: ignore[typeddict-item]
    if "programs" in data:
        import capo_partnercentral_channel.types.program_list

        out["programs"] = (
            capo_partnercentral_channel.types.program_list.deserialize_aws_json_1_0(
                data["programs"]
            )
        )
    return out

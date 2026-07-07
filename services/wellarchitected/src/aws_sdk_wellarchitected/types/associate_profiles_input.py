"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AssociateProfilesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_arns
    import aws_sdk_wellarchitected.types.workload_id


class AssociateProfilesInput(TypedDict, closed=True):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    profile_arns: NotRequired["aws_sdk_wellarchitected.types.profile_arns.ProfileArns"]
    """<p>The list of profile ARNs to associate with the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateProfilesInput) -> dict:
    out: dict = {}
    if "profile_arns" in value:
        import aws_sdk_wellarchitected.types.profile_arns

        out["ProfileArns"] = aws_sdk_wellarchitected.types.profile_arns.serialize_json(
            value["profile_arns"]
        )
    return out


def deserialize_json(data: dict) -> AssociateProfilesInput:
    out: AssociateProfilesInput = {}  # type: ignore[typeddict-item]
    if "ProfileArns" in data:
        import aws_sdk_wellarchitected.types.profile_arns

        out["profile_arns"] = (
            aws_sdk_wellarchitected.types.profile_arns.deserialize_json(
                data["ProfileArns"]
            )
        )
    return out

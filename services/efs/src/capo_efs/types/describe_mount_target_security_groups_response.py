"""Generated from Smithy shape ``com.amazonaws.efs#DescribeMountTargetSecurityGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.security_groups


class DescribeMountTargetSecurityGroupsResponse(TypedDict, closed=True):
    security_groups: "capo_efs.types.security_groups.SecurityGroups"
    """<p>An array of security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMountTargetSecurityGroupsResponse) -> dict:
    out: dict = {}
    import capo_efs.types.security_groups

    out["SecurityGroups"] = capo_efs.types.security_groups.serialize_json(
        value["security_groups"]
    )
    return out


def deserialize_json(data: dict) -> DescribeMountTargetSecurityGroupsResponse:
    out: DescribeMountTargetSecurityGroupsResponse = {}  # type: ignore[typeddict-item]
    if "SecurityGroups" in data:
        import capo_efs.types.security_groups

        out["security_groups"] = capo_efs.types.security_groups.deserialize_json(
            data["SecurityGroups"]
        )
    else:
        raise DeserializationError(
            "DescribeMountTargetSecurityGroupsResponse.security_groups required"
        )
    return out

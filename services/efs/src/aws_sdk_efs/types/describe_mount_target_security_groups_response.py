"""Generated from Smithy shape ``com.amazonaws.efs#DescribeMountTargetSecurityGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.security_groups


class DescribeMountTargetSecurityGroupsResponse(TypedDict):
    security_groups: "aws_sdk_efs.types.security_groups.SecurityGroups"
    """<p>An array of security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMountTargetSecurityGroupsResponse) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.security_groups

    out["SecurityGroups"] = aws_sdk_efs.types.security_groups.serialize_json(
        value["security_groups"]
    )
    return out


def deserialize_json(data: dict) -> DescribeMountTargetSecurityGroupsResponse:
    out: DescribeMountTargetSecurityGroupsResponse = {}  # type: ignore[typeddict-item]
    if "SecurityGroups" in data:
        import aws_sdk_efs.types.security_groups

        out["security_groups"] = aws_sdk_efs.types.security_groups.deserialize_json(
            data["SecurityGroups"]
        )
    else:
        raise DeserializationError(
            "DescribeMountTargetSecurityGroupsResponse.security_groups required"
        )
    return out

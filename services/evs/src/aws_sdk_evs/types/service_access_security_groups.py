"""Generated from Smithy shape ``com.amazonaws.evs#ServiceAccessSecurityGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_evs.types.security_groups


class ServiceAccessSecurityGroups(TypedDict, closed=True):
    security_groups: NotRequired["aws_sdk_evs.types.security_groups.SecurityGroups"]
    """<p>The security groups that allow service access.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceAccessSecurityGroups) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import aws_sdk_evs.types.security_groups

        out["securityGroups"] = (
            aws_sdk_evs.types.security_groups.serialize_aws_json_1_0(
                value["security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceAccessSecurityGroups:
    out: ServiceAccessSecurityGroups = {}  # type: ignore[typeddict-item]
    if "securityGroups" in data:
        import aws_sdk_evs.types.security_groups

        out["security_groups"] = (
            aws_sdk_evs.types.security_groups.deserialize_aws_json_1_0(
                data["securityGroups"]
            )
        )
    return out

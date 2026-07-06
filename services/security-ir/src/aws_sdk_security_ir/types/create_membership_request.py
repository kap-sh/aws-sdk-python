"""Generated from Smithy shape ``com.amazonaws.securityir#CreateMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.incident_response_team
    import aws_sdk_security_ir.types.membership_name
    import aws_sdk_security_ir.types.opt_in_features
    import aws_sdk_security_ir.types.tag_map


class CreateMembershipRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""
    membership_name: "aws_sdk_security_ir.types.membership_name.MembershipName"
    """<p>Required element used in combination with CreateMembership to create a name for the membership.</p>"""
    incident_response_team: (
        "aws_sdk_security_ir.types.incident_response_team.IncidentResponseTeam"
    )
    """<p>Required element used in combination with CreateMembership to add customer incident response team members and trusted partners to the membership. </p>"""
    opt_in_features: NotRequired[
        "aws_sdk_security_ir.types.opt_in_features.OptInFeatures"
    ]
    """<p>Optional element to enable the monitoring and investigation opt-in features for the service.</p>"""
    tags: NotRequired["aws_sdk_security_ir.types.tag_map.TagMap"]
    """<p>Optional element for customer configured tags.</p>"""
    cover_entire_organization: "bool"
    """<p>The <code>coverEntireOrganization</code> parameter is a boolean flag that determines whether the membership should be applied to the entire Amazon Web Services Organization. When set to true, the membership will be created for all accounts within the organization. When set to false, the membership will only be created for specified accounts. </p> <p>This parameter is optional. If not specified, the default value is false.</p> <ul> <li> <p>If set to <i>true</i>: The membership will automatically include all existing and future accounts in the Amazon Web Services Organization. </p> </li> <li> <p>If set to <i>false</i>: The membership will only apply to explicitly specified accounts. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["membershipName"] = value["membership_name"]
    import aws_sdk_security_ir.types.incident_response_team

    out["incidentResponseTeam"] = (
        aws_sdk_security_ir.types.incident_response_team.serialize_json(
            value["incident_response_team"]
        )
    )
    if "opt_in_features" in value:
        import aws_sdk_security_ir.types.opt_in_features

        out["optInFeatures"] = aws_sdk_security_ir.types.opt_in_features.serialize_json(
            value["opt_in_features"]
        )
    if "tags" in value:
        import aws_sdk_security_ir.types.tag_map

        out["tags"] = aws_sdk_security_ir.types.tag_map.serialize_json(value["tags"])
    out["coverEntireOrganization"] = value.get("cover_entire_organization", True)
    return out


def deserialize_json(data: dict) -> CreateMembershipRequest:
    out: CreateMembershipRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "membershipName" in data:
        out["membership_name"] = data["membershipName"]
    else:
        raise DeserializationError("CreateMembershipRequest.membership_name required")
    if "incidentResponseTeam" in data:
        import aws_sdk_security_ir.types.incident_response_team

        out["incident_response_team"] = (
            aws_sdk_security_ir.types.incident_response_team.deserialize_json(
                data["incidentResponseTeam"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMembershipRequest.incident_response_team required"
        )
    if "optInFeatures" in data:
        import aws_sdk_security_ir.types.opt_in_features

        out["opt_in_features"] = (
            aws_sdk_security_ir.types.opt_in_features.deserialize_json(
                data["optInFeatures"]
            )
        )
    if "tags" in data:
        import aws_sdk_security_ir.types.tag_map

        out["tags"] = aws_sdk_security_ir.types.tag_map.deserialize_json(data["tags"])
    if "coverEntireOrganization" in data:
        out["cover_entire_organization"] = data["coverEntireOrganization"]
    else:
        out["cover_entire_organization"] = True
    return out

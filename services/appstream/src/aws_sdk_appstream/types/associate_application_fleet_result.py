"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateApplicationFleetResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application_fleet_association


class AssociateApplicationFleetResult(TypedDict):
    application_fleet_association: NotRequired[
        "aws_sdk_appstream.types.application_fleet_association.ApplicationFleetAssociation"
    ]
    """<p>If fleet name is specified, this returns the list of applications that are associated to it. If application ARN is specified, this returns the list of fleets to which it is associated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateApplicationFleetResult) -> dict:
    out: dict = {}
    if "application_fleet_association" in value:
        import aws_sdk_appstream.types.application_fleet_association

        out["ApplicationFleetAssociation"] = (
            aws_sdk_appstream.types.application_fleet_association.serialize_aws_json_1_1(
                value["application_fleet_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateApplicationFleetResult:
    out: AssociateApplicationFleetResult = {}  # type: ignore[typeddict-item]
    if "ApplicationFleetAssociation" in data:
        import aws_sdk_appstream.types.application_fleet_association

        out["application_fleet_association"] = (
            aws_sdk_appstream.types.application_fleet_association.deserialize_aws_json_1_1(
                data["ApplicationFleetAssociation"]
            )
        )
    return out

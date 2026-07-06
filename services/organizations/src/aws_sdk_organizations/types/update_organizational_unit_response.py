"""Generated from Smithy shape ``com.amazonaws.organizations#UpdateOrganizationalUnitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.organizational_unit


class UpdateOrganizationalUnitResponse(TypedDict, closed=True):
    organizational_unit: NotRequired[
        "aws_sdk_organizations.types.organizational_unit.OrganizationalUnit"
    ]
    """<p>A structure that contains the details about the specified OU, including its new name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOrganizationalUnitResponse) -> dict:
    out: dict = {}
    if "organizational_unit" in value:
        import aws_sdk_organizations.types.organizational_unit

        out["OrganizationalUnit"] = (
            aws_sdk_organizations.types.organizational_unit.serialize_aws_json_1_1(
                value["organizational_unit"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOrganizationalUnitResponse:
    out: UpdateOrganizationalUnitResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationalUnit" in data:
        import aws_sdk_organizations.types.organizational_unit

        out["organizational_unit"] = (
            aws_sdk_organizations.types.organizational_unit.deserialize_aws_json_1_1(
                data["OrganizationalUnit"]
            )
        )
    return out

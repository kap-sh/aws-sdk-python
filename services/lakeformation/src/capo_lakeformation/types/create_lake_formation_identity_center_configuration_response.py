"""Generated from Smithy shape ``com.amazonaws.lakeformation#CreateLakeFormationIdentityCenterConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.application_arn


class CreateLakeFormationIdentityCenterConfigurationResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_lakeformation.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lake Formation application integrated with IAM Identity Center.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: CreateLakeFormationIdentityCenterConfigurationResponse,
) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_json(
    data: dict,
) -> CreateLakeFormationIdentityCenterConfigurationResponse:
    out: CreateLakeFormationIdentityCenterConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out

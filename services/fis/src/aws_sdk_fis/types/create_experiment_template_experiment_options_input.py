"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateExperimentOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.account_targeting
    import aws_sdk_fis.types.empty_target_resolution_mode


class CreateExperimentTemplateExperimentOptionsInput(TypedDict):
    account_targeting: NotRequired[
        "aws_sdk_fis.types.account_targeting.AccountTargeting"
    ]
    """<p>Specifies the account targeting setting for experiment options.</p>"""
    empty_target_resolution_mode: NotRequired[
        "aws_sdk_fis.types.empty_target_resolution_mode.EmptyTargetResolutionMode"
    ]
    """<p>Specifies the empty target resolution mode for experiment options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateExperimentOptionsInput) -> dict:
    out: dict = {}
    if "account_targeting" in value:
        import aws_sdk_fis.types.account_targeting

        out["accountTargeting"] = aws_sdk_fis.types.account_targeting.serialize_json(
            value["account_targeting"]
        )
    if "empty_target_resolution_mode" in value:
        import aws_sdk_fis.types.empty_target_resolution_mode

        out["emptyTargetResolutionMode"] = (
            aws_sdk_fis.types.empty_target_resolution_mode.serialize_json(
                value["empty_target_resolution_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateExperimentOptionsInput:
    out: CreateExperimentTemplateExperimentOptionsInput = {}  # type: ignore[typeddict-item]
    if "accountTargeting" in data:
        import aws_sdk_fis.types.account_targeting

        out["account_targeting"] = aws_sdk_fis.types.account_targeting.deserialize_json(
            data["accountTargeting"]
        )
    if "emptyTargetResolutionMode" in data:
        import aws_sdk_fis.types.empty_target_resolution_mode

        out["empty_target_resolution_mode"] = (
            aws_sdk_fis.types.empty_target_resolution_mode.deserialize_json(
                data["emptyTargetResolutionMode"]
            )
        )
    return out

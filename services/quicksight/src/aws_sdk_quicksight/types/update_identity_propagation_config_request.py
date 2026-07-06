"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateIdentityPropagationConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.authorized_targets_list
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.service_type


class UpdateIdentityPropagationConfigRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the identity propagation configuration that you want to update.</p>"""
    service: "aws_sdk_quicksight.types.service_type.ServiceType"
    """<p>The name of the Amazon Web Services service that contains the authorized targets that you want to add or update.</p>"""
    authorized_targets: NotRequired[
        "aws_sdk_quicksight.types.authorized_targets_list.AuthorizedTargetsList"
    ]
    """<p>Specifies a list of application ARNs that represent the authorized targets for a service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdentityPropagationConfigRequest) -> dict:
    out: dict = {}
    if "authorized_targets" in value:
        import aws_sdk_quicksight.types.authorized_targets_list

        out["AuthorizedTargets"] = (
            aws_sdk_quicksight.types.authorized_targets_list.serialize_json(
                value["authorized_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIdentityPropagationConfigRequest:
    out: UpdateIdentityPropagationConfigRequest = {}  # type: ignore[typeddict-item]
    if "AuthorizedTargets" in data:
        import aws_sdk_quicksight.types.authorized_targets_list

        out["authorized_targets"] = (
            aws_sdk_quicksight.types.authorized_targets_list.deserialize_json(
                data["AuthorizedTargets"]
            )
        )
    return out

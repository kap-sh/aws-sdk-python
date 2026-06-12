"""Generated from Smithy shape ``com.amazonaws.licensemanager#Options``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.activation_override_behavior


class Options(TypedDict):
    activation_override_behavior: NotRequired[
        "aws_sdk_license_manager.types.activation_override_behavior.ActivationOverrideBehavior"
    ]
    """<p>An activation option for your grant that determines the behavior of activating a grant. Activation options can only be used with granted licenses sourced from the Amazon Web Services Marketplace. Additionally, the operation must specify the value of <code>ACTIVE</code> for the <code>Status</code> parameter.</p> <ul> <li> <p>As a license administrator, you can optionally specify an <code>ActivationOverrideBehavior</code> when activating a grant.</p> </li> <li> <p>As a grantor, you can optionally specify an <code>ActivationOverrideBehavior</code> when you activate a grant for a grantee account in your organization.</p> </li> <li> <p>As a grantee, if the grantor creating the distributed grant doesn’t specify an <code>ActivationOverrideBehavior</code>, you can optionally specify one when you are activating the grant.</p> </li> </ul> <dl> <dt>DISTRIBUTED_GRANTS_ONLY</dt> <dd> <p>Use this value to activate a grant without replacing any member account’s active grants for the same product.</p> </dd> <dt>ALL_GRANTS_PERMITTED_BY_ISSUER</dt> <dd> <p>Use this value to activate a grant and disable other active grants in any member accounts for the same product. This action will also replace their previously activated grants with this activated grant.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Options) -> dict:
    out: dict = {}
    if "activation_override_behavior" in value:
        import aws_sdk_license_manager.types.activation_override_behavior

        out["ActivationOverrideBehavior"] = (
            aws_sdk_license_manager.types.activation_override_behavior.serialize_aws_json_1_1(
                value["activation_override_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Options:
    out: Options = {}  # type: ignore[typeddict-item]
    if "ActivationOverrideBehavior" in data:
        import aws_sdk_license_manager.types.activation_override_behavior

        out["activation_override_behavior"] = (
            aws_sdk_license_manager.types.activation_override_behavior.deserialize_aws_json_1_1(
                data["ActivationOverrideBehavior"]
            )
        )
    return out

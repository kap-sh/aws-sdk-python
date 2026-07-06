"""Generated from Smithy shape ``com.amazonaws.ssooidc#AwsAdditionalDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.identity_context


class AwsAdditionalDetails(TypedDict, closed=True):
    identity_context: NotRequired[
        "aws_sdk_sso_oidc.types.identity_context.IdentityContext"
    ]
    """<p>The trusted context assertion is signed and encrypted by STS. It provides access to <code>sts:identity_context</code> claim in the <code>idToken</code> without JWT parsing</p> <p>Identity context comprises information that Amazon Web Services services use to make authorization decisions when they receive requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAdditionalDetails) -> dict:
    out: dict = {}
    if "identity_context" in value:
        out["identityContext"] = value["identity_context"]
    return out


def deserialize_json(data: dict) -> AwsAdditionalDetails:
    out: AwsAdditionalDetails = {}  # type: ignore[typeddict-item]
    if "identityContext" in data:
        out["identity_context"] = data["identityContext"]
    return out

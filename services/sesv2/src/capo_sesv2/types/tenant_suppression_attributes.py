"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantSuppressionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.suppression_list_reasons
    import capo_sesv2.types.suppression_list_scope


class TenantSuppressionAttributes(TypedDict, closed=True):
    suppressed_reasons: NotRequired[
        "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>A list that contains the reasons that email addresses are automatically added to the suppression list for the tenant. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a hard bounce.</p> </li> </ul>"""
    suppression_scope: NotRequired[
        "capo_sesv2.types.suppression_list_scope.SuppressionListScope"
    ]
    """<p>The suppression scope for the tenant. Can be one of the following:</p> <ul> <li> <p> <code>TENANT</code> – The tenant uses its own suppression list.</p> </li> <li> <p> <code>ACCOUNT</code> – The tenant uses the account-level suppression list.</p> </li> </ul> <note> <p>If you don't specify a suppression scope, the tenant defaults to <code>ACCOUNT</code> scope and uses the account-level suppression list.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TenantSuppressionAttributes) -> dict:
    out: dict = {}
    if "suppressed_reasons" in value:
        import capo_sesv2.types.suppression_list_reasons

        out["SuppressedReasons"] = (
            capo_sesv2.types.suppression_list_reasons.serialize_json(
                value["suppressed_reasons"]
            )
        )
    if "suppression_scope" in value:
        import capo_sesv2.types.suppression_list_scope

        out["SuppressionScope"] = (
            capo_sesv2.types.suppression_list_scope.serialize_json(
                value["suppression_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> TenantSuppressionAttributes:
    out: TenantSuppressionAttributes = {}  # type: ignore[typeddict-item]
    if "SuppressedReasons" in data:
        import capo_sesv2.types.suppression_list_reasons

        out["suppressed_reasons"] = (
            capo_sesv2.types.suppression_list_reasons.deserialize_json(
                data["SuppressedReasons"]
            )
        )
    if "SuppressionScope" in data:
        import capo_sesv2.types.suppression_list_scope

        out["suppression_scope"] = (
            capo_sesv2.types.suppression_list_scope.deserialize_json(
                data["SuppressionScope"]
            )
        )
    return out

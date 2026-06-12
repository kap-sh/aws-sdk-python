"""Generated from Smithy shape ``com.amazonaws.sesv2#PutTenantSuppressionAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_list_reasons
    import aws_sdk_sesv2.types.suppression_list_scope
    import aws_sdk_sesv2.types.tenant_name


class PutTenantSuppressionAttributesRequest(TypedDict):
    tenant_name: "aws_sdk_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to configure suppression list preferences for.</p>"""
    suppressed_reasons: NotRequired[
        "aws_sdk_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>A list that contains the reasons that email addresses are automatically added to the suppression list for the tenant. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a hard bounce.</p> </li> </ul>"""
    suppression_scope: NotRequired[
        "aws_sdk_sesv2.types.suppression_list_scope.SuppressionListScope"
    ]
    """<p>The suppression scope for the tenant. Specify <code>TENANT</code> to use the tenant's own suppression list, or <code>ACCOUNT</code> to use the account-level suppression list.</p> <note> <p>If you don't specify a suppression scope, the tenant defaults to <code>ACCOUNT</code> scope and uses the account-level suppression list.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTenantSuppressionAttributesRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    if "suppressed_reasons" in value:
        import aws_sdk_sesv2.types.suppression_list_reasons

        out["SuppressedReasons"] = (
            aws_sdk_sesv2.types.suppression_list_reasons.serialize_json(
                value["suppressed_reasons"]
            )
        )
    if "suppression_scope" in value:
        import aws_sdk_sesv2.types.suppression_list_scope

        out["SuppressionScope"] = (
            aws_sdk_sesv2.types.suppression_list_scope.serialize_json(
                value["suppression_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutTenantSuppressionAttributesRequest:
    out: PutTenantSuppressionAttributesRequest = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    else:
        raise DeserializationError(
            "PutTenantSuppressionAttributesRequest.tenant_name required"
        )
    if "SuppressedReasons" in data:
        import aws_sdk_sesv2.types.suppression_list_reasons

        out["suppressed_reasons"] = (
            aws_sdk_sesv2.types.suppression_list_reasons.deserialize_json(
                data["SuppressedReasons"]
            )
        )
    if "SuppressionScope" in data:
        import aws_sdk_sesv2.types.suppression_list_scope

        out["suppression_scope"] = (
            aws_sdk_sesv2.types.suppression_list_scope.deserialize_json(
                data["SuppressionScope"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.suppressed_destination_attributes
    import aws_sdk_sesv2.types.suppression_list_reason
    import aws_sdk_sesv2.types.tenant_name
    import aws_sdk_sesv2.types.timestamp


class SuppressedDestination(TypedDict):
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The email address that is on the suppression list for your account or for a specific tenant.</p>"""
    reason: "aws_sdk_sesv2.types.suppression_list_reason.SuppressionListReason"
    """<p>The reason that the address was added to the suppression list for your account or for a specific tenant.</p>"""
    last_update_time: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>The date and time when the suppressed destination was last updated, shown in Unix time format.</p>"""
    attributes: NotRequired[
        "aws_sdk_sesv2.types.suppressed_destination_attributes.SuppressedDestinationAttributes"
    ]
    """<p>An optional value that can contain additional information about the reasons that the address was added to the suppression list for your account or for a specific tenant.</p>"""
    tenant_name: NotRequired["aws_sdk_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant that the suppressed destination belongs to. This field is present only when the suppressed destination is on a tenant's suppression list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestination) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    import aws_sdk_sesv2.types.suppression_list_reason

    out["Reason"] = aws_sdk_sesv2.types.suppression_list_reason.serialize_json(
        value["reason"]
    )
    import aws_sdk_sesv2.types.timestamp

    out["LastUpdateTime"] = aws_sdk_sesv2.types.timestamp.serialize_json(
        value["last_update_time"]
    )
    if "attributes" in value:
        import aws_sdk_sesv2.types.suppressed_destination_attributes

        out["Attributes"] = (
            aws_sdk_sesv2.types.suppressed_destination_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    return out


def deserialize_json(data: dict) -> SuppressedDestination:
    out: SuppressedDestination = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("SuppressedDestination.email_address required")
    if "Reason" in data:
        import aws_sdk_sesv2.types.suppression_list_reason

        out["reason"] = aws_sdk_sesv2.types.suppression_list_reason.deserialize_json(
            data["Reason"]
        )
    else:
        raise DeserializationError("SuppressedDestination.reason required")
    if "LastUpdateTime" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_update_time"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    else:
        raise DeserializationError("SuppressedDestination.last_update_time required")
    if "Attributes" in data:
        import aws_sdk_sesv2.types.suppressed_destination_attributes

        out["attributes"] = (
            aws_sdk_sesv2.types.suppressed_destination_attributes.deserialize_json(
                data["Attributes"]
            )
        )
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    return out

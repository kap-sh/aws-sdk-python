"""Generated from Smithy shape ``com.amazonaws.acm#PutAccountConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.expiry_events_configuration
    import capo_acm.types.idempotency_token


class PutAccountConfigurationRequest(TypedDict, closed=True):
    expiry_events: NotRequired[
        "capo_acm.types.expiry_events_configuration.ExpiryEventsConfiguration"
    ]
    """<p>Specifies expiration events associated with an account.</p>"""
    idempotency_token: "capo_acm.types.idempotency_token.IdempotencyToken"
    """<p>Customer-chosen string used to distinguish between calls to <code>PutAccountConfiguration</code>. Idempotency tokens time out after one hour. If you call <code>PutAccountConfiguration</code> multiple times with the same unexpired idempotency token, ACM treats it as the same request and returns the original result. If you change the idempotency token for each call, ACM treats each call as a new request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccountConfigurationRequest) -> dict:
    out: dict = {}
    if "expiry_events" in value:
        import capo_acm.types.expiry_events_configuration

        out["ExpiryEvents"] = (
            capo_acm.types.expiry_events_configuration.serialize_aws_json_1_1(
                value["expiry_events"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccountConfigurationRequest:
    out: PutAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ExpiryEvents" in data:
        import capo_acm.types.expiry_events_configuration

        out["expiry_events"] = (
            capo_acm.types.expiry_events_configuration.deserialize_aws_json_1_1(
                data["ExpiryEvents"]
            )
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "PutAccountConfigurationRequest.idempotency_token required"
        )
    return out

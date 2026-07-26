"""Generated from Smithy shape ``com.amazonaws.acm#GetAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.expiry_events_configuration


class GetAccountConfigurationResponse(TypedDict, closed=True):
    expiry_events: NotRequired[
        "capo_acm.types.expiry_events_configuration.ExpiryEventsConfiguration"
    ]
    """<p>Expiration events configuration options associated with the Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "expiry_events" in value:
        import capo_acm.types.expiry_events_configuration

        out["ExpiryEvents"] = (
            capo_acm.types.expiry_events_configuration.serialize_aws_json_1_1(
                value["expiry_events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountConfigurationResponse:
    out: GetAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ExpiryEvents" in data:
        import capo_acm.types.expiry_events_configuration

        out["expiry_events"] = (
            capo_acm.types.expiry_events_configuration.deserialize_aws_json_1_1(
                data["ExpiryEvents"]
            )
        )
    return out

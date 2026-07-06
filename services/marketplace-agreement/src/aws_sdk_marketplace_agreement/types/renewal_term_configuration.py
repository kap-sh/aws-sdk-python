"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RenewalTermConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.boolean


class RenewalTermConfiguration(TypedDict, closed=True):
    enable_auto_renew: "aws_sdk_marketplace_agreement.types.boolean.Boolean"
    """<p>Defines whether the acceptor has chosen to auto-renew the agreement at the end of its lifecycle. Can be set to <code>True</code> or <code>False</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RenewalTermConfiguration) -> dict:
    out: dict = {}
    out["enableAutoRenew"] = value["enable_auto_renew"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RenewalTermConfiguration:
    out: RenewalTermConfiguration = {}  # type: ignore[typeddict-item]
    if "enableAutoRenew" in data:
        out["enable_auto_renew"] = data["enableAutoRenew"]
    else:
        raise DeserializationError(
            "RenewalTermConfiguration.enable_auto_renew required"
        )
    return out

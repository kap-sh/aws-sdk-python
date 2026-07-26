"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RoutingType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.failover_type


class RoutingType(TypedDict, closed=True):
    failover: NotRequired[
        "capo_cognito_identity_provider.types.failover_type.FailoverType"
    ]
    """<p>The failover configuration that specifies the secondary region and health check settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingType) -> dict:
    out: dict = {}
    if "failover" in value:
        import capo_cognito_identity_provider.types.failover_type

        out["Failover"] = (
            capo_cognito_identity_provider.types.failover_type.serialize_aws_json_1_1(
                value["failover"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingType:
    out: RoutingType = {}  # type: ignore[typeddict-item]
    if "Failover" in data:
        import capo_cognito_identity_provider.types.failover_type

        out["failover"] = (
            capo_cognito_identity_provider.types.failover_type.deserialize_aws_json_1_1(
                data["Failover"]
            )
        )
    return out

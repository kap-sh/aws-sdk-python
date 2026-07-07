"""Generated from Smithy shape ``com.amazonaws.interconnect#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.bandwidths
    import aws_sdk_interconnect.types.environment_id
    import aws_sdk_interconnect.types.environment_state
    import aws_sdk_interconnect.types.location
    import aws_sdk_interconnect.types.product_type
    import aws_sdk_interconnect.types.provider
    import aws_sdk_interconnect.types.remote_account_identifier_type


class Environment(TypedDict, closed=True):
    provider: "aws_sdk_interconnect.types.provider.Provider"
    """<p>The provider on the remote side of this <a>Connection</a>.</p>"""
    location: "aws_sdk_interconnect.types.location.Location"
    """<p>The provider specific location on the remote side of this <a>Connection</a>.</p>"""
    environment_id: "aws_sdk_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of this <a>Environment</a> </p>"""
    state: "aws_sdk_interconnect.types.environment_state.EnvironmentState"
    """<p>The state of the <a>Environment</a>. Possible values:</p> <ul> <li> <p> <code>available</code>: The environment is available and new <a>Connection</a> objects can be requested.</p> </li> <li> <p> <code>limited</code>: The environment is available, but overall capacity is limited. The set of available bandwidths </p> </li> <li> <p> <code>unavailable</code>: The environment is currently unavailable.</p> </li> </ul>"""
    bandwidths: "aws_sdk_interconnect.types.bandwidths.Bandwidths"
    """<p>The sets of bandwidths that are available and supported on this environment.</p>"""
    type: "aws_sdk_interconnect.types.product_type.ProductType"
    """<p>The specific product type of <a>Connection</a> objects provided by this <a>Environment</a>.</p>"""
    activation_page_url: NotRequired["str"]
    """<p>An HTTPS URL on the remote partner portal where the Activation Key should be brought to complete the creation process.</p>"""
    remote_identifier_type: NotRequired[
        "aws_sdk_interconnect.types.remote_account_identifier_type.RemoteAccountIdentifierType"
    ]
    """<p>The type of identifying information that should be supplied to the <code>remoteAccount</code> parameter of a <a>CreateConnection</a> call for this specific Environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Environment) -> dict:
    out: dict = {}
    import aws_sdk_interconnect.types.provider

    out["provider"] = aws_sdk_interconnect.types.provider.serialize_aws_json_1_0(
        value["provider"]
    )
    out["location"] = value["location"]
    out["environmentId"] = value["environment_id"]
    import aws_sdk_interconnect.types.environment_state

    out["state"] = aws_sdk_interconnect.types.environment_state.serialize_aws_json_1_0(
        value["state"]
    )
    import aws_sdk_interconnect.types.bandwidths

    out["bandwidths"] = aws_sdk_interconnect.types.bandwidths.serialize_aws_json_1_0(
        value["bandwidths"]
    )
    out["type"] = value["type"]
    if "activation_page_url" in value:
        out["activationPageUrl"] = value["activation_page_url"]
    if "remote_identifier_type" in value:
        import aws_sdk_interconnect.types.remote_account_identifier_type

        out["remoteIdentifierType"] = (
            aws_sdk_interconnect.types.remote_account_identifier_type.serialize_aws_json_1_0(
                value["remote_identifier_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        import aws_sdk_interconnect.types.provider

        out["provider"] = aws_sdk_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    else:
        raise DeserializationError("Environment.provider required")
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("Environment.location required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("Environment.environment_id required")
    if "state" in data:
        import aws_sdk_interconnect.types.environment_state

        out["state"] = (
            aws_sdk_interconnect.types.environment_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        raise DeserializationError("Environment.state required")
    if "bandwidths" in data:
        import aws_sdk_interconnect.types.bandwidths

        out["bandwidths"] = (
            aws_sdk_interconnect.types.bandwidths.deserialize_aws_json_1_0(
                data["bandwidths"]
            )
        )
    else:
        raise DeserializationError("Environment.bandwidths required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Environment.type required")
    if "activationPageUrl" in data:
        out["activation_page_url"] = data["activationPageUrl"]
    if "remoteIdentifierType" in data:
        import aws_sdk_interconnect.types.remote_account_identifier_type

        out["remote_identifier_type"] = (
            aws_sdk_interconnect.types.remote_account_identifier_type.deserialize_aws_json_1_0(
                data["remoteIdentifierType"]
            )
        )
    return out

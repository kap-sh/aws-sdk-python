"""Generated from Smithy shape ``com.amazonaws.firehose#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.connectivity
    import capo_firehose.types.role_arn


class AuthenticationConfiguration(TypedDict, closed=True):
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The ARN of the role used to access the Amazon MSK cluster.</p>"""
    connectivity: "capo_firehose.types.connectivity.Connectivity"
    """<p>The type of connectivity used to access the Amazon MSK cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    import capo_firehose.types.connectivity

    out["Connectivity"] = capo_firehose.types.connectivity.serialize_aws_json_1_1(
        value["connectivity"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("AuthenticationConfiguration.role_arn required")
    if "Connectivity" in data:
        import capo_firehose.types.connectivity

        out["connectivity"] = capo_firehose.types.connectivity.deserialize_aws_json_1_1(
            data["Connectivity"]
        )
    else:
        raise DeserializationError("AuthenticationConfiguration.connectivity required")
    return out

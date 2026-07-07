"""Generated from Smithy shape ``com.amazonaws.connect#SignInConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.sign_in_distribution_list


class SignInConfig(TypedDict, closed=True):
    distributions: (
        "aws_sdk_connect.types.sign_in_distribution_list.SignInDistributionList"
    )
    """<p>Information about traffic distributions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignInConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.sign_in_distribution_list

    out["Distributions"] = (
        aws_sdk_connect.types.sign_in_distribution_list.serialize_json(
            value["distributions"]
        )
    )
    return out


def deserialize_json(data: dict) -> SignInConfig:
    out: SignInConfig = {}  # type: ignore[typeddict-item]
    if "Distributions" in data:
        import aws_sdk_connect.types.sign_in_distribution_list

        out["distributions"] = (
            aws_sdk_connect.types.sign_in_distribution_list.deserialize_json(
                data["Distributions"]
            )
        )
    else:
        raise DeserializationError("SignInConfig.distributions required")
    return out

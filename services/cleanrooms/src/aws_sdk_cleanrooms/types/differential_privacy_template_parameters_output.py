"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyTemplateParametersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.epsilon
    import aws_sdk_cleanrooms.types.users_noise_per_query


class DifferentialPrivacyTemplateParametersOutput(TypedDict, closed=True):
    epsilon: "aws_sdk_cleanrooms.types.epsilon.Epsilon"
    """<p>The epsilon value that you specified.</p>"""
    users_noise_per_query: (
        "aws_sdk_cleanrooms.types.users_noise_per_query.UsersNoisePerQuery"
    )
    """<p>Noise added per query is measured in terms of the number of users whose contributions you want to obscure. This value governs the rate at which the privacy budget is depleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyTemplateParametersOutput) -> dict:
    out: dict = {}
    out["epsilon"] = value["epsilon"]
    out["usersNoisePerQuery"] = value["users_noise_per_query"]
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyTemplateParametersOutput:
    out: DifferentialPrivacyTemplateParametersOutput = {}  # type: ignore[typeddict-item]
    if "epsilon" in data:
        out["epsilon"] = data["epsilon"]
    else:
        raise DeserializationError(
            "DifferentialPrivacyTemplateParametersOutput.epsilon required"
        )
    if "usersNoisePerQuery" in data:
        out["users_noise_per_query"] = data["usersNoisePerQuery"]
    else:
        raise DeserializationError(
            "DifferentialPrivacyTemplateParametersOutput.users_noise_per_query required"
        )
    return out

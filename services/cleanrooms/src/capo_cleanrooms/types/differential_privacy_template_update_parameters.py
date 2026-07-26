"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyTemplateUpdateParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.epsilon
    import capo_cleanrooms.types.users_noise_per_query


class DifferentialPrivacyTemplateUpdateParameters(TypedDict, closed=True):
    epsilon: NotRequired["capo_cleanrooms.types.epsilon.Epsilon"]
    """<p>The updated epsilon value that you want to use.</p>"""
    users_noise_per_query: NotRequired[
        "capo_cleanrooms.types.users_noise_per_query.UsersNoisePerQuery"
    ]
    """<p>The updated value of noise added per query. It is measured in terms of the number of users whose contributions you want to obscure. This value governs the rate at which the privacy budget is depleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyTemplateUpdateParameters) -> dict:
    out: dict = {}
    if "epsilon" in value:
        out["epsilon"] = value["epsilon"]
    if "users_noise_per_query" in value:
        out["usersNoisePerQuery"] = value["users_noise_per_query"]
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyTemplateUpdateParameters:
    out: DifferentialPrivacyTemplateUpdateParameters = {}  # type: ignore[typeddict-item]
    if "epsilon" in data:
        out["epsilon"] = data["epsilon"]
    if "usersNoisePerQuery" in data:
        out["users_noise_per_query"] = data["usersNoisePerQuery"]
    return out

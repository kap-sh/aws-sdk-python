"""Generated from Smithy shape ``com.amazonaws.appconfigdata#StartConfigurationSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfigdata.types.token


class StartConfigurationSessionResponse(TypedDict):
    initial_configuration_token: NotRequired["aws_sdk_appconfigdata.types.token.Token"]
    """<p>Token encapsulating state about the configuration session. Provide this token to the <code>GetLatestConfiguration</code> API to retrieve configuration data.</p> <important> <p>This token should only be used once in your first call to <code>GetLatestConfiguration</code>. You <i>must</i> use the new token in the <code>GetLatestConfiguration</code> response (<code>NextPollConfigurationToken</code>) in each subsequent call to <code>GetLatestConfiguration</code>.</p> <p>The <code>InitialConfigurationToken</code> and <code>NextPollConfigurationToken</code> should only be used once. To support long poll use cases, the tokens are valid for up to 24 hours. If a <code>GetLatestConfiguration</code> call uses an expired token, the system returns <code>BadRequestException</code>.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationSessionResponse) -> dict:
    out: dict = {}
    if "initial_configuration_token" in value:
        out["InitialConfigurationToken"] = value["initial_configuration_token"]
    return out


def deserialize_json(data: dict) -> StartConfigurationSessionResponse:
    out: StartConfigurationSessionResponse = {}  # type: ignore[typeddict-item]
    if "InitialConfigurationToken" in data:
        out["initial_configuration_token"] = data["InitialConfigurationToken"]
    return out

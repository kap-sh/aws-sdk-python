"""Generated from Smithy shape ``com.amazonaws.appconfigdata#GetLatestConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfigdata.types.token


class GetLatestConfigurationRequest(TypedDict, closed=True):
    configuration_token: "aws_sdk_appconfigdata.types.token.Token"
    """<p>Token describing the current state of the configuration session. To obtain a token, first call the <a>StartConfigurationSession</a> API. Note that every call to <code>GetLatestConfiguration</code> will return a new <code>ConfigurationToken</code> (<code>NextPollConfigurationToken</code> in the response) and <i>must</i> be provided to subsequent <code>GetLatestConfiguration</code> API calls.</p> <important> <p>This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a <code>GetLatestConfiguration</code> call uses an expired token, the system returns <code>BadRequestException</code>.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLatestConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLatestConfigurationRequest:
    out: GetLatestConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

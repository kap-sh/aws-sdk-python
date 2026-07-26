"""Generated from Smithy shape ``com.amazonaws.securityhub#ServiceNowUpdateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ServiceNowUpdateConfiguration(TypedDict, closed=True):
    secret_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the ServiceNow credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowUpdateConfiguration) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> ServiceNowUpdateConfiguration:
    out: ServiceNowUpdateConfiguration = {}  # type: ignore[typeddict-item]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out

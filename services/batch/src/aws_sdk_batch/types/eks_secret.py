"""Generated from Smithy shape ``com.amazonaws.batch#EksSecret``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.string


class EksSecret(TypedDict):
    secret_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the secret. The name must be allowed as a DNS subdomain name. For more information, see <a href=\"https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names\">DNS subdomain names</a> in the <i>Kubernetes documentation</i>.</p>"""
    optional: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Specifies whether the secret or the secret's keys must be defined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksSecret) -> dict:
    out: dict = {}
    if "secret_name" in value:
        out["secretName"] = value["secret_name"]
    if "optional" in value:
        out["optional"] = value["optional"]
    return out


def deserialize_json(data: dict) -> EksSecret:
    out: EksSecret = {}  # type: ignore[typeddict-item]
    if "secretName" in data:
        out["secret_name"] = data["secretName"]
    if "optional" in data:
        out["optional"] = data["optional"]
    return out

"""Generated from Smithy shape ``com.amazonaws.apprunner#IngressConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.boolean


class IngressConfiguration(TypedDict, closed=True):
    is_publicly_accessible: "capo_apprunner.types.boolean.Boolean"
    """<p>Specifies whether your App Runner service is publicly accessible. To make the service publicly accessible set it to <code>True</code>. To make the service privately accessible, from only within an Amazon VPC set it to <code>False</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressConfiguration) -> dict:
    out: dict = {}
    out["IsPubliclyAccessible"] = value.get("is_publicly_accessible", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressConfiguration:
    out: IngressConfiguration = {}  # type: ignore[typeddict-item]
    if "IsPubliclyAccessible" in data:
        out["is_publicly_accessible"] = data["IsPubliclyAccessible"]
    else:
        out["is_publicly_accessible"] = False
    return out

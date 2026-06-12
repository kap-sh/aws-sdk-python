"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Principal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.principal_arn
    import aws_sdk_lex_models_v2.types.service_principal


class Principal(TypedDict):
    service: NotRequired[
        "aws_sdk_lex_models_v2.types.service_principal.ServicePrincipal"
    ]
    """<p>The name of the Amazon Web Services service that should allowed or denied access to an Amazon Lex action.</p>"""
    arn: NotRequired["aws_sdk_lex_models_v2.types.principal_arn.PrincipalArn"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Principal) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> Principal:
    out: Principal = {}  # type: ignore[typeddict-item]
    if "service" in data:
        out["service"] = data["service"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out

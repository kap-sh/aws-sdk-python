"""Generated from Smithy shape ``com.amazonaws.pcs#JwtAuth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.jwt_key


class JwtAuth(TypedDict, closed=True):
    jwt_key: NotRequired["capo_pcs.types.jwt_key.JwtKey"]
    """<p>The JWT key for Slurm REST API authentication.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JwtAuth) -> dict:
    out: dict = {}
    if "jwt_key" in value:
        import capo_pcs.types.jwt_key

        out["jwtKey"] = capo_pcs.types.jwt_key.serialize_aws_json_1_0(value["jwt_key"])
    return out


def deserialize_aws_json_1_0(data: dict) -> JwtAuth:
    out: JwtAuth = {}  # type: ignore[typeddict-item]
    if "jwtKey" in data:
        import capo_pcs.types.jwt_key

        out["jwt_key"] = capo_pcs.types.jwt_key.deserialize_aws_json_1_0(data["jwtKey"])
    return out

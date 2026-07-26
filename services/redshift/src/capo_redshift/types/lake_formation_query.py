"""Generated from Smithy shape ``com.amazonaws.redshift#LakeFormationQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.service_authorization


class LakeFormationQuery(TypedDict, closed=True):
    authorization: NotRequired[
        "capo_redshift.types.service_authorization.ServiceAuthorization"
    ]
    """<p>Determines whether the query scope is enabled or disabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LakeFormationQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "authorization" in value:
        import capo_redshift.types.service_authorization

        capo_redshift.types.service_authorization.serialize_query(
            value["authorization"], pairs, f"{prefix}.Authorization"
        )


def deserialize_query(el: Element) -> LakeFormationQuery:
    out: LakeFormationQuery = {}  # type: ignore[typeddict-item]
    child_authorization = el.find("Authorization")
    if child_authorization is not None:
        import capo_redshift.types.service_authorization

        out["authorization"] = (
            capo_redshift.types.service_authorization.deserialize_query(
                child_authorization
            )
        )
    return out

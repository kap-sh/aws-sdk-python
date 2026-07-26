from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    interpolate,
)


class EndpointParams:
    def __init__(
        self,
        *,
        Region: str | None = None,
        UseFIPS: bool | None = None,
        UseDualStack: bool | None = None,
        Endpoint: str | None = None,
    ):
        self.Region = Region
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    _locals["PartitionResult"] = aws_partition(p.Region)
    if _locals["PartitionResult"] is not None:
        if p.UseFIPS is True:
            if p.UseDualStack is True:
                return Endpoint(
                    url=interpolate(
                        "https://data-signer-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
        if p.UseFIPS is True:
            return Endpoint(
                url=interpolate(
                    "https://data-signer-fips.{Region}.{PartitionResult#dnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
        if p.UseDualStack is True:
            return Endpoint(
                url=interpolate(
                    "https://data-signer.{Region}.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
        return Endpoint(
            url=interpolate(
                "https://data-signer.{Region}.{PartitionResult#dnsSuffix}", p, _locals
            ),
            properties={},
            headers={},
        )
    raise EndpointError("No endpoint rules matched")

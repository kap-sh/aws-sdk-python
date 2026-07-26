from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    get_attr,
    interpolate,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseFIPS: bool | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if not (p.Region is not None):
        _locals["PartitionResult"] = aws_partition(interpolate("us-west-2", p, _locals))
        if _locals["PartitionResult"] is not None:
            if p.UseFIPS is True:
                if (
                    get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    )
                    is False
                ):
                    raise EndpointError(
                        interpolate("Partition does not support FIPS.", p, _locals)
                    )
                return Endpoint(
                    url=interpolate(
                        "https://codecatalyst-fips.global.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            return Endpoint(
                url=interpolate(
                    "https://codecatalyst.global.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if p.UseFIPS is True:
                if (
                    get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    )
                    is False
                ):
                    raise EndpointError(
                        interpolate("Partition does not support FIPS.", p, _locals)
                    )
                return Endpoint(
                    url=interpolate(
                        "https://codecatalyst-fips.global.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            return Endpoint(
                url=interpolate(
                    "https://codecatalyst.global.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
    raise EndpointError("No endpoint rules matched")
